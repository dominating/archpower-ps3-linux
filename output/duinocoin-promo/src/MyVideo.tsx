import { AbsoluteFill, Sequence, useCurrentFrame, useVideoConfig, spring, interpolate, Img } from "remotion";
import { Cpu, Zap, Coins, Server } from "lucide-react";

export const MyVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Background animation
  const bgRotation = interpolate(frame, [0, 300], [0, 360]);

  return (
    <AbsoluteFill className="bg-slate-950 items-center justify-center text-white overflow-hidden font-sans">
      {/* Dynamic Background */}
      <AbsoluteFill>
        <div 
          className="absolute inset-0 bg-gradient-to-br from-orange-600/20 via-transparent to-red-600/20"
          style={{ transform: `scale(2) rotate(${bgRotation}deg)` }}
        />
        <div className="absolute inset-0 bg-black " />
      </AbsoluteFill>

      {/* Scene 1: The Hook */}
      <Sequence from={0} durationInFrames={100}>
        <Scene1 frame={frame} fps={fps} />
      </Sequence>

      {/* Scene 2: The Solution */}
      <Sequence from={80} durationInFrames={120}>
        <Scene2 frame={frame - 80} fps={fps} />
      </Sequence>

      {/* Scene 3: The Outro */}
      <Sequence from={180} durationInFrames={120}>
        <Scene3 frame={frame - 180} fps={fps} />
      </Sequence>
    </AbsoluteFill>
  );
};

const Scene1 = ({ frame, fps }: { frame: number; fps: number }) => {
  const scale = spring({ frame, fps, config: { damping: 14 } });
  const opacity = interpolate(frame, [80, 100], [1, 0], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill className="items-center justify-center" style={{ opacity }}>
      <div style={{ transform: `scale(${scale})` }} className="flex flex-col items-center">
        <Server className="w-32 h-32 text-orange-500 mb-8" />
        <h1 className="text-6xl font-black tracking-tight mb-4">Turn idle hardware</h1>
        <h2 className="text-5xl font-bold text-orange-400">into crypto rewards.</h2>
      </div>
    </AbsoluteFill>
  );
};

const Scene2 = ({ frame, fps }: { frame: number; fps: number }) => {
  const scale = spring({ frame, fps, config: { damping: 14 } });
  const yOffset = interpolate(frame, [0, 20], [100, 0], { extrapolateRight: "clamp", extrapolateLeft: "clamp" });
  const opacity = interpolate(frame, [100, 120], [1, 0], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill className="items-center justify-center" style={{ opacity }}>
      <div style={{ transform: `scale(${scale}) translateY(${yOffset}px)` }} className="flex flex-col items-center bg-slate-900/80 p-16 rounded-3xl border border-slate-800 shadow-2xl">
        <div className="flex gap-8 mb-8">
          <Cpu className="w-24 h-24 text-blue-400" />
          <Zap className="w-24 h-24 text-yellow-400" />
        </div>
        <h1 className="text-6xl font-black text-white mb-4">Mine DuinoCoin (DUCO)</h1>
        <h2 className="text-4xl text-slate-300">Directly on ESP32-S2 USB Dongles</h2>
      </div>
    </AbsoluteFill>
  );
};

const Scene3 = ({ frame, fps }: { frame: number; fps: number }) => {
  const scale = spring({ frame, fps, from: 0.8, to: 1, config: { damping: 14 } });
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateLeft: "clamp" });

  return (
    <AbsoluteFill className="items-center justify-center" style={{ opacity }}>
      <div style={{ transform: `scale(${scale})` }} className="flex flex-col items-center">
        <Coins className="w-40 h-40 text-orange-500 mb-12 drop-shadow-[0_0_30px_rgba(249,115,22,0.5)]" />
        <h1 className="text-7xl font-black mb-6">Silent. Headless. Passive.</h1>
        <div className="bg-orange-500/20 text-orange-300 px-8 py-4 rounded-full text-3xl font-bold border border-orange-500/50">
          Get Started at duinocoin.com
        </div>
      </div>
    </AbsoluteFill>
  );
};
