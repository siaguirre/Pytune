import { useEffect, useState } from "react";
import logoPytune from "../../assets/logo.png";
import { ExampleCard } from "../../components/ExampleCard/ExampleCard";
import { ExampleCardHistory } from "../../components/ExampleCardHistory/ExampleCardHistory";
import { examplesPrompts } from "../../constants/examplesPrompts";
import { BACKEND_URL } from "../../constants/config";
import { Loader } from "../../components/Loader/Loader";
import { Select } from "../../components/Select/Select";
import { HistoryItem, SelectOption } from "../../types/common";

export const Home = () => {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [selectedGender, setSelectedGender] = useState("");
  const [selectedInstrument, setSelectedInstrument] = useState("");
  const [selectedMood, setSelectedMood] = useState("");
  const [history, setHistory] = useState<HistoryItem[]>();
  const [selectOptions, setSelectOptions] = useState<{
    gender: SelectOption[];
    instrument: SelectOption[];
    mood: SelectOption[];
  }>({
    gender: [],
    instrument: [],
    mood: [],
  });

  const updatePromptFromSelections = (
    gender: string,
    instrument: string,
    mood: string
  ) => {
    const parts = [];
    if (gender) {
      const genderLabel = selectOptions.gender.find(
        (g) => g.value === gender
      )?.label;
      parts.push(`género ${genderLabel}`);
    }
    if (instrument) {
      const instrumentLabel = selectOptions.instrument.find(
        (i) => i.value === instrument
      )?.label;
      parts.push(`con ${instrumentLabel}`);
    }
    if (mood) {
      const moodLabel = selectOptions.mood.find((m) => m.value === mood)?.label;
      parts.push(`que suene ${moodLabel?.toLowerCase()}`);
    }

    if (parts.length > 0) {
      setPrompt(`Generar una melodía de ${parts.join(" ")}`);
    }
  };

  const handleRandomize = () => {
    const randomGender =
      selectOptions.gender[
        Math.floor(Math.random() * selectOptions.gender.length)
      ]?.value || "";
    const randomInstrument =
      selectOptions.instrument[
        Math.floor(Math.random() * selectOptions.instrument.length)
      ]?.value || "";
    const randomMood =
      selectOptions.mood[Math.floor(Math.random() * selectOptions.mood.length)]
        ?.value || "";

    setSelectedGender(randomGender);
    setSelectedInstrument(randomInstrument);
    setSelectedMood(randomMood);

    updatePromptFromSelections(randomGender, randomInstrument, randomMood);
  };

  useEffect(() => {
    updatePromptFromSelections(
      selectedGender,
      selectedInstrument,
      selectedMood
    );
  }, [selectedGender, selectedInstrument, selectedMood]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [historyResponse, suggestionsResponse] = await Promise.all([
          fetch(`${BACKEND_URL}get_history`),
          fetch(`${BACKEND_URL}get_suggestions`),
        ]);

        const historyData = await historyResponse.json();
        const suggestionsData = await suggestionsResponse.json();

        setHistory(historyData);

        // Transformar los datos del backend al formato necesario para los selectores
        const transformedOptions = {
          gender: suggestionsData.genero.map((item: string) => ({
            value: item
              .toLowerCase()
              .normalize("NFD")
              .replace(/[\u0300-\u036f]/g, ""),
            label: item,
          })),
          instrument: suggestionsData.instrumento.map((item: string) => ({
            value: item
              .toLowerCase()
              .normalize("NFD")
              .replace(/[\u0300-\u036f]/g, "")
              .replace(/ /g, "_"),
            label: item,
          })),
          mood: suggestionsData.estilo.map((item: string) => ({
            value: item
              .toLowerCase()
              .normalize("NFD")
              .replace(/[\u0300-\u036f]/g, ""),
            label: item,
          })),
        };

        setSelectOptions(transformedOptions);
      } catch (error) {
        console.error("Error al obtener datos del servidor:", error);
      }
    };

    fetchData();
  }, []);

  const handleSubmit = async () => {
    if (!prompt.trim()) {
      alert("Por favor ingresa un prompt");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(`${BACKEND_URL}send_prompt`, {
        method: "POST",
        body: (() => {
          const formData = new FormData();
          formData.append("prompt", prompt);
          return formData;
        })(),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.status} ${response.statusText}`);
      }

      const contentType = response.headers.get("Content-Type");

      if (
        contentType?.includes("application/octet-stream") ||
        contentType?.includes("audio/")
      ) {
        // Si es un archivo de audio
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "pytune_melody.wav";
        document.body.appendChild(a);
        a.click();

        a.remove();
        URL.revokeObjectURL(url);
      } else {
        // Si es una respuesta JSON
        const data = await response.json();
        console.log("Respuesta del servidor:", data);

        if (data.message) {
          alert(data.message);
        }
      }
    } catch (error) {
      console.error("Error al conectar con el servidor:", error);
      alert(
        "Error al generar la música. Verifica que el servidor esté ejecutándose."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen w-full bg-gradient-to-b from-purple-300 to-indigo-400 flex flex-col items-center px-4 py-6 sm:px-6 sm:py-8 lg:px-8">
      {/* Header */}
      <header className="flex flex-col items-center mb-6 sm:mb-8">
        <img
          src={logoPytune}
          alt="Logo"
          className="w-24 h-24 sm:w-32 sm:h-32 lg:w-40 lg:h-40 mb-2"
        />
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold mb-3 sm:mb-4 text-center">
          Py<span className="text-indigo-600">Tune</span>
        </h1>
        <p className="text-base sm:text-lg lg:text-xl mb-6 sm:mb-8 font-semibold text-center max-w-2xl px-4">
          ¿Qué tipo de melodía te gustaría crear hoy?
        </p>
      </header>

      {/* Controles de selección */}
      <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 mb-6 w-full max-w-4xl px-4">
        <Select
          options={selectOptions.gender}
          disabled={loading}
          value={selectedGender}
          onChange={setSelectedGender}
          placeholder="Selecciona un género"
        />

        <Select
          options={selectOptions.instrument}
          disabled={loading}
          value={selectedInstrument}
          onChange={setSelectedInstrument}
          placeholder="Selecciona un instrumento"
        />

        <Select
          options={selectOptions.mood}
          disabled={loading}
          value={selectedMood}
          onChange={setSelectedMood}
          placeholder="Selecciona un estado de ánimo"
        />
      </div>

      {/* Input y botón de generación */}
      <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 mb-8 w-full max-w-4xl px-4">
        <input
          type="text"
          placeholder={
            loading
              ? "Generando..."
              : "Describe el estilo de melodía que quieres generar..."
          }
          className="flex-1 p-3 sm:p-4 rounded-lg bg-white text-sm sm:text-base placeholder:text-gray-500"
          value={prompt}
          disabled={loading}
          onChange={(e) => setPrompt(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSubmit()}
        />
        <div className="flex gap-2">
          <button
            onClick={handleRandomize}
            disabled={loading}
            className="px-6 py-3 sm:px-8 sm:py-4 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition cursor-pointer shadow-xl font-semibold disabled:opacity-50 disabled:cursor-not-allowed text-sm sm:text-base whitespace-nowrap"
            aria-label="Randomizar prompt"
          >
            Aleatorio
          </button>
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="px-6 py-3 sm:px-8 sm:py-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition cursor-pointer shadow-xl font-semibold disabled:opacity-50 disabled:cursor-not-allowed text-sm sm:text-base whitespace-nowrap"
          >
            Generar
          </button>
        </div>
      </div>

      {loading ? (
        <div className="flex justify-center items-center py-12">
          <Loader />
        </div>
      ) : (
        <div className="w-full max-w-6xl px-4">
          {/* Sección de ejemplos */}
          <div className="flex items-center gap-3 sm:gap-5 mb-6 sm:mb-8">
            <div className="flex-1 border-t border-gray-600" />
            <h3 className="font-semibold text-sm sm:text-base lg:text-lg text-center whitespace-nowrap">
              Ejemplos de instrucciones
            </h3>
            <div className="flex-1 border-t border-gray-600" />
          </div>

          <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 sm:gap-4 mb-8 sm:mb-12">
            {examplesPrompts.map((ejemplo, idx) => (
              <ExampleCard
                key={idx}
                title={ejemplo}
                onPress={() => setPrompt(ejemplo)}
              />
            ))}
          </section>

          {/* Sección de historial */}
          <div className="flex items-center gap-3 sm:gap-5 mb-6 sm:mb-8">
            <div className="flex-1 border-t border-gray-600" />
            <h3 className="font-semibold text-sm sm:text-base lg:text-lg text-center whitespace-nowrap">
              Historial de Búsquedas
            </h3>
            <div className="flex-1 border-t border-gray-600" />
          </div>

          <section className="flex flex-col gap-3 sm:gap-4 mb-8">
            {history && history.length > 0 ? (
              <>
                {history?.map((item: HistoryItem, idx: number) => (
                  <ExampleCardHistory
                    key={idx}
                    title={item.prompt}
                    onPress={() => setPrompt(item.prompt)}
                  />
                ))}
              </>
            ) : (
              <div className="flex justify-center items-center h-16 sm:h-20 bg-white rounded-lg shadow-md">
                <p className="text-gray-600 text-sm sm:text-base">
                  No hay historial de búsquedas
                </p>
              </div>
            )}
          </section>
        </div>
      )}

      {/* Footer */}
      <footer className="mt-8 sm:mt-12 px-4">
        <p className="text-center text-xs sm:text-sm text-gray-700 max-w-4xl">
          2025 Pytune. UADE - Simón Aguirre - Ezequiel Mónaco - Jerónimo Podestá
          - Valentín Romero
        </p>
      </footer>
    </main>
  );
};
