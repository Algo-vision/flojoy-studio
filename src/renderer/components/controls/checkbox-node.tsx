import { useControlBlock } from "@/renderer/hooks/useControlBlock";
import { WidgetProps } from "@/renderer/types/control";
import { toast } from "sonner";
import { Checkbox } from "@/renderer/components/ui/checkbox";
import { CheckedState } from "@radix-ui/react-checkbox";
import WidgetLabel from "@/renderer/components/common/widget-label";

export const CheckboxNode = ({ id, data }: WidgetProps) => {
  const { block, updateBlockParameter } = useControlBlock(data.blockId);
  if (!block) {
    return <div className="text-2xl text-red-500">NOT FOUND</div>;
  }

  const name = block.data.label;
  const paramVal = block.data.ctrls[data.blockParameter].value;

  const handleChange = (state: CheckedState) => {
    const res = updateBlockParameter(
      block.id,
      data.blockParameter,
      Boolean(state.valueOf()),
    );
    if (res.isErr()) {
      toast.error("Error updating block parameter", {
        description: res.error.message,
      });
    }
  };

  return (
    <div className="flex flex-col items-center rounded-md">
      <WidgetLabel
        label={data.label}
        placeholder={`${name} (${data.blockParameter})`}
        widgetId={id}
      />
      <div className="py-1" />
      <Checkbox
        className="nodrag h-6 w-6"
        checked={paramVal as boolean}
        onCheckedChange={handleChange}
      />
    </div>
  );
};