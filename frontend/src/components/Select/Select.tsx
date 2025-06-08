import { SelectOption } from "../../types/common";

interface SelectProps {
  options: SelectOption[];
  disabled?: boolean;
  onChange?: (value: string) => void;
  value?: string;
  placeholder?: string;
  className?: string;
}

export const Select = ({ 
  options, 
  disabled = false, 
  onChange, 
  value, 
  placeholder,
  className = "" 
}: SelectProps) => {
  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    if (onChange) {
      onChange(event.target.value);
    }
  };

  return (
    <select
      disabled={disabled}
      value={value}
      onChange={handleChange}
      className={`flex-1 px-3 py-2 sm:px-4 sm:py-3 rounded-xl bg-white hover:shadow-xl transition cursor-pointer font-semibold text-sm sm:text-base min-w-0 border border-gray-200 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed ${className}`}
    >
      {placeholder && (
        <option value="" disabled>
          {placeholder}
        </option>
      )}
      {options.map((option) => (
        <option key={option.value} value={option.value}>
          {option.label}
        </option>
      ))}
    </select>
  );
}; 