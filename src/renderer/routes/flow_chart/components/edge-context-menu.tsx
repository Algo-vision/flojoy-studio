import { ContextMenuAction } from "@/renderer/components/common/context-menu-action";
import { useDeleteEdge } from "@/renderer/stores/project";
import { EdgeMenuInfo } from "@/renderer/types/context-menu";
import { X } from "lucide-react";


export type EdgeContextMenuInfo = EdgeMenuInfo 
type Props = EdgeContextMenuInfo & {
  onClick?: () => void;
 
};
export default function EdgeContextMenu({
  edge,
  top,
  left,
  right,
  bottom,
  onClick,
}:Props) {




  
  const deleteEdge = useDeleteEdge();

  return (
    <div
      style={{ top, left, right, bottom }}
      className="absolute z-50 rounded-md border bg-background"
      onClick={onClick}
      data-testid={"block-context-menu"}
    >
      <ContextMenuAction
        testId="context-delete-edge"
        onClick={()=>{deleteEdge(edge.id)}}
        icon={X}
      >
        Remove Link
      </ContextMenuAction>

    </div>
  );
}
