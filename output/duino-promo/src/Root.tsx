import { Composition } from "remotion";
import { MyVideo } from "./MyVideo";

export const Root = () => {
  return (
    <>
      <Composition
        id="DuinoPromo"
        component={MyVideo}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
