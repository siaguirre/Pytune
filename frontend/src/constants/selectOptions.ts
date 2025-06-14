import { SelectOptions } from "../types/common";

export const selectOptions: SelectOptions = {
  mood: [
    { value: "", label: "Estado de Ánimo" },
    { value: "feliz", label: "Feliz" },
    { value: "relajado", label: "Relajado" },
    { value: "triste", label: "Triste" },
    { value: "epico", label: "Épico" },
  ],
  instrument: [
    { value: "", label: "Instrumento" },
    { value: "guitarra", label: "Guitarra" },
    { value: "violin", label: "Violín" },
    { value: "piano", label: "Piano" },
    { value: "sintetizador", label: "Sintetizador" },
  ],
  gender: [
    { value: "", label: "Género" },
    { value: "pop", label: "Pop" },
    { value: "rock", label: "Rock" },
    { value: "jazz", label: "Jazz" },
    { value: "clasico", label: "Clásico" },
  ],
};
