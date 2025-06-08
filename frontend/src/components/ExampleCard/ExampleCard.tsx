interface ExampleCardProps {
  title: string;
  onPress: () => void;
}

export const ExampleCard = ({ title, onPress }: ExampleCardProps) => {
  return (
    <div
      onClick={onPress}
      className="flex justify-center items-center border-l-4 border-black bg-white p-6 rounded-lg shadow hover:shadow-xl transition cursor-pointer checked:bg-red"
    >
      {title}
    </div>
  );
};
