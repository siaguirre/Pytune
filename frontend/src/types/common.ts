// Tipos comunes para todo el proyecto

export interface SelectOption {
  value: string;
  label: string;
}

export interface SelectOptions {
  mood: SelectOption[];
  instrument: SelectOption[];
  gender: SelectOption[];
}

export interface HistoryItem {
  prompt: string;
  fecha_introduccion: string;
}
