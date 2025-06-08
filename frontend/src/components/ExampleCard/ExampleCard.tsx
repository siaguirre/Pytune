interface ExampleCardProps {
  title: string;
  onPress: () => void;
}

export const ExampleCard = ({ title, onPress }: ExampleCardProps) => {
  return (
    <div
      onClick={onPress}
      className="flex justify-center items-center border-l-4 border-black bg-white p-4 sm:p-6 rounded-lg shadow hover:shadow-xl transition cursor-pointer min-h-[80px] sm:min-h-[100px] text-center"
    >
      <span className="text-sm sm:text-base font-medium text-gray-800 leading-relaxed">
        {title}
      </span>
    </div>
  );
};
