import { useFlowChartState } from "../../../hooks/useFlowChartState";
import HandleComponent from "../components/HandleComponent";
import NodeComponent from "../components/NodeComponent";
import { NodeStyle } from "../style/NodeStyle";
import { CustomNodeProps, ElementsData } from "../types/CustomNodeProps";

const highlightShadow = {
  'LINSPACE': {boxShadow: '0 0 50px 15px #48abe0'},
  'HISTOGRAM': {boxShadow: '0 0 50px 15px #48abe0'},
  'SCATTER': {boxShadow: '0 0 50px 15px #48abe0'},
  'SURFACE3D': {boxShadow: '0 0 50px 15px #48abe0'},
  'SCATTER3D': {boxShadow: '0 0 50px 15px #48abe0'},
  'BAR': {boxShadow: '0 0 50px 15px #48abe0'},
  'LINE': {boxShadow: '0 0 50px 15px #48abe0'},
  'SINE': {boxShadow: 'rgb(116 24 181 / 97%) 0px 0px 50px 15px'},
  'RAND': {boxShadow: 'rgb(116 24 181 / 97%) 0px 0px 50px 15px'},
  'CONSTANT': {boxShadow: 'rgb(116 24 181 / 97%) 0px 0px 50px 15px'},
  'MULTIPLY': {boxShadow: 'rgb(112 96 13) 0px 0px 50px 15px', background: '#78640f96'},
  'ADD': {boxShadow: 'rgb(112 96 13) 0px 0px 50px 15px', background: '#78640f96'},

} 
const getboxShadow = (data: ElementsData) =>{
  return highlightShadow[data.func]
}


const CustomNode = ({ data }: CustomNodeProps) => {
  const { uiTheme } = useFlowChartState();
  const params = data.inputs || [];
  
  return (
    <div style={{
      ...(data.running && getboxShadow(data)),
      ...(data.failed && {
        boxShadow: 'rgb(183 0 0) 0px 0px 50px 15px'
      })
    }}>
    <div
      style={{
        position: "relative",
        ...NodeStyle(data, uiTheme),
        height: "fit-content",
        minHeight: 115,
        ...(params.length > 0 && { paddingBottom: "8px" }),
      }}
    >
      <NodeComponent data={data} uiTheme={uiTheme} params={params} />
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          height: params.length > 0 ? (params.length + 1) * 30 : "fit-content",
        }}
      >
        <HandleComponent data={data} inputs={params} />
      </div>
    </div>
    </div>
  );
};

export default CustomNode;