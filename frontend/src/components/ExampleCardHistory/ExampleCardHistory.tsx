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
      className="flex justify-between items-center border-l-4 border-indigo-700 bg-white p-6 rounded-lg shadow hover:shadow-xl transition cursor-pointer "
    >
      {title}
      <FontAwesomeIcon icon={faArrowRight} />
    </div>
  );
};
