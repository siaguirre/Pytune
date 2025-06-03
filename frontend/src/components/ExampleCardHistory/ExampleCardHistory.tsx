import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

interface ExampleCardProps {
  title: string;
  onPress: () => void;
}

export const ExampleCardHistory = ({ title, onPress }: ExampleCardProps) => {
  return (
    <div
      onClick={onPress}
      className="flex justify-between items-center border-l-4 border-indigo-700 bg-white p-4 sm:p-6 rounded-lg shadow hover:shadow-xl transition cursor-pointer min-h-[60px] sm:min-h-[70px]"
    >
      <span className="text-sm sm:text-base font-medium text-gray-800 leading-relaxed flex-1 pr-3">
        {title}
      </span>
      <FontAwesomeIcon icon={faArrowRight} className="text-indigo-600 text-sm sm:text-base flex-shrink-0" />
    </div>
  );
};
