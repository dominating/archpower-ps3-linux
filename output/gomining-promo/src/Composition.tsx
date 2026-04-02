import { AbsoluteFill, Sequence, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";
import { Bitcoin, Zap, Activity, CreditCard } from "lucide-react";
import React from "react";

const AnimatedBackground = ({ frame }: { frame: number }) => {
  const rotation = interpolate(frame, [0, 400], [0, 360]);
  return (
    <AbsoluteFill className="bg-slate-950 items-center justify-center overflow-hidden">
      <div 
        style={{ transform: `rotate(${rotation}deg)` }}
        className="absolute w-[150vw] h-[150vw] bg-gradient-to-tr from-amber-500/20 via-orange-500/10 to-transparent rounded-full blur-[100px] opacity-60"
      />
      <div 
        style={{ transform: `rotate(-${rotation * 0.5}deg)` }}
        className="absolute w-[100vw] h-[100vw] bg-gradient-to-bl from-amber-600/10 via-yellow-500/5 to-transparent rounded-full blur-[80px] opacity-50"
      />
    </AbsoluteFill>
  );
};

const IntroScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const scale = spring({ frame, fps, from: 0.5, to: 1, config: { damping: 15 } });
  const opacity = interpolate(frame, [0, 15], [0, 1]);
  const exitOpacity = interpolate(frame, [75, 90], [1, 0], { extrapolateRight: "clamp" });
  
  return (
    <AbsoluteFill className="items-center justify-center flex-col text-white" style={{ opacity: exitOpacity }}>
      <div style={{ transform: `scale(${scale})`, opacity }} className="flex flex-col items-center gap-6">
        <div className="p-6 bg-amber-500/20 rounded-full border border-amber-500/30">
          <Bitcoin size={80} className="text-amber-500" />
        </div>
        <h1 className="text-7xl font-bold tracking-tight text-center">
          Earn Bitcoin.<br/>
          <span className="text-amber-500">Use Bitcoin.</span>
        </h1>
        <p className="text-2xl text-slate-300">One App.</p>
      </div>
    </AbsoluteFill>
  );
};

const SolutionScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const slideY = interpolate(frame, [0, 20], [100, 0], { extrapolateRight: "clamp" });
  const opacity = interpolate(frame, [0, 20], [0, 1]);
  const exitOpacity = interpolate(frame, [105, 120], [1, 0], { extrapolateRight: "clamp" });
  
  return (
    <AbsoluteFill className="items-center justify-center flex-col text-white" style={{ opacity: exitOpacity }}>
      <div style={{ transform: `translateY(${slideY}px)`, opacity }} className="flex flex-col items-center gap-8 w-full max-w-4xl px-8">
        <h2 className="text-6xl font-bold tracking-tight text-center">
          Mining Made <span className="text-amber-500">Easy</span>
        </h2>
        
        <div className="grid grid-cols-2 gap-8 w-full mt-8">
          <div className="bg-slate-900/80 p-8 rounded-2xl border border-slate-800 flex flex-col items-center text-center gap-4">
            <Zap size={48} className="text-amber-400" />
            <h3 className="text-2xl font-semibold">Own Hashrate</h3>
            <p className="text-slate-400 text-lg">We handle the hardware & maintenance.</p>
          </div>
          <div className="bg-slate-900/80 p-8 rounded-2xl border border-slate-800 flex flex-col items-center text-center gap-4">
            <Bitcoin size={48} className="text-amber-400" />
            <h3 className="text-2xl font-semibold">Daily Rewards</h3>
            <p className="text-slate-400 text-lg">Stable, transparent payouts you control.</p>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const StatsScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const scale = spring({ frame, fps, from: 0.8, to: 1, config: { damping: 12 } });
  const opacity = interpolate(frame, [0, 15], [0, 1]);
  const exitOpacity = interpolate(frame, [90, 105], [1, 0], { extrapolateRight: "clamp" });
  
  return (
    <AbsoluteFill className="items-center justify-center flex-col text-white" style={{ opacity: exitOpacity }}>
      <div style={{ transform: `scale(${scale})`, opacity }} className="flex flex-col items-center gap-12 w-full">
        <h2 className="text-5xl font-bold">The Power of <span className="text-amber-500">GoMining</span></h2>
        
        <div className="flex gap-12 mt-4">
          <div className="flex flex-col items-center gap-2">
            <Activity size={40} className="text-amber-500 mb-2" />
            <span className="text-6xl font-bold">14M+</span>
            <span className="text-xl text-slate-400 uppercase tracking-widest">TH/s Hashrate</span>
          </div>
          <div className="w-px h-24 bg-slate-800" />
          <div className="flex flex-col items-center gap-2">
            <Bitcoin size={40} className="text-amber-500 mb-2" />
            <span className="text-6xl font-bold">5,267+</span>
            <span className="text-xl text-slate-400 uppercase tracking-widest">BTC Earned</span>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const CTAScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const slideY = spring({ frame, fps, from: 50, to: 0, config: { damping: 15 } });
  const opacity = interpolate(frame, [0, 15], [0, 1]);
  
  return (
    <AbsoluteFill className="items-center justify-center flex-col text-white bg-amber-600/10">
      <div style={{ transform: `translateY(${slideY}px)`, opacity }} className="flex flex-col items-center gap-8">
        <div className="p-4 bg-amber-500 rounded-full text-slate-950 mb-2">
          <CreditCard size={64} />
        </div>
        <h2 className="text-7xl font-bold tracking-tight text-center">
          Unlock your <br/>
          Bitcoin potential.
        </h2>
        
        <div className="mt-8 px-10 py-5 bg-white text-slate-950 text-3xl font-bold rounded-full shadow-[0_0_40px_rgba(245,158,11,0.4)]">
          gomining.com
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const MyComposition = () => {
  const frame = useCurrentFrame();
  
  return (
    <AbsoluteFill>
      <AnimatedBackground frame={frame} />
      
      <Sequence from={0} durationInFrames={90}>
        <IntroScene />
      </Sequence>
      
      <Sequence from={90} durationInFrames={120}>
        <SolutionScene />
      </Sequence>
      
      <Sequence from={210} durationInFrames={105}>
        <StatsScene />
      </Sequence>
      
      <Sequence from={315} durationInFrames={90}>
        <CTAScene />
      </Sequence>
    </AbsoluteFill>
  );
};
