import { AbsoluteFill, Sequence, useCurrentFrame, useVideoConfig, interpolate, spring, Img, staticFile } from "remotion";
import { Leaf, Cpu, Globe, Rocket } from "lucide-react";

export const MyVideo = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill className="bg-[#111] text-white overflow-hidden font-sans">
      {/* Dynamic Background */}
      <div className="absolute inset-0 opacity-20">
        <div 
          className="absolute w-[800px] h-[800px] bg-brand-orange rounded-full blur-[100px]"
          style={{
            transform: `translate(${Math.sin(frame / 60) * 100}px, ${Math.cos(frame / 60) * 100}px)`,
            top: '-20%',
            left: '-10%'
          }}
        />
        <div 
          className="absolute w-[600px] h-[600px] bg-brand-red rounded-full blur-[100px]"
          style={{
            transform: `translate(${Math.cos(frame / 50) * 100}px, ${Math.sin(frame / 50) * 100}px)`,
            bottom: '-20%',
            right: '-10%'
          }}
        />
      </div>

      <Sequence from={0} durationInFrames={120}>
        <IntroScene />
      </Sequence>
      
      <Sequence from={100} durationInFrames={150}>
        <FeaturesScene />
      </Sequence>

      <Sequence from={230} durationInFrames={120}>
        <HardwareScene />
      </Sequence>

      <Sequence from={330} durationInFrames={120}>
        <CTAScene />
      </Sequence>

    </AbsoluteFill>
  );
};

const IntroScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const logoScale = spring({ frame, fps, from: 0, to: 1, durationInFrames: 30, config: { damping: 12 } });
  const textOpacity = interpolate(frame, [15, 30], [0, 1], { extrapolateRight: "clamp" });
  const textY = spring({ frame: frame - 15, fps, from: 50, to: 0, durationInFrames: 30, config: { damping: 14 } });
  
  const exitOpacity = interpolate(frame, [100, 120], [1, 0], { extrapolateRight: "clamp" });
  const exitScale = interpolate(frame, [100, 120], [1, 1.5], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill className="justify-center items-center flex-col" style={{ opacity: exitOpacity, transform: `scale(${exitScale})` }}>
      <div style={{ transform: `scale(${logoScale})` }} className="mb-12">
        <Img src={staticFile("images/brand/logo.png")} className="w-64 h-64 object-contain drop-shadow-2xl" />
      </div>
      <div style={{ opacity: textOpacity, transform: `translateY(${textY}px)` }} className="text-center">
        <h1 className="text-8xl font-black mb-6 tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-brand-orange to-yellow-400">Duino-Coin</h1>
        <p className="text-3xl text-gray-300 font-medium tracking-wide">Simple, eco-friendly, centralized coin.</p>
      </div>
    </AbsoluteFill>
  );
};

const FeaturesScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const containerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });
  const titleY = spring({ frame, fps, from: -100, to: 0, durationInFrames: 30, config: { damping: 12 } });

  const exitOpacity = interpolate(frame, [130, 150], [1, 0], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill className="justify-center items-center" style={{ opacity: containerOpacity * exitOpacity }}>
      <h2 style={{ transform: `translateY(${titleY}px)` }} className="absolute top-32 text-6xl font-bold tracking-tight text-white/90">Mining for <span className="text-brand-orange">Everyone</span></h2>
      
      <div className="flex gap-16">
        <FeatureCard icon={Leaf} title="Eco-Friendly" desc="Energy efficient algorithms" delay={15} />
        <FeatureCard icon={Globe} title="Accessible" desc="Available everywhere" delay={30} />
        <FeatureCard icon={Rocket} title="Community" desc="Fast-growing network" delay={45} />
      </div>
    </AbsoluteFill>
  );
};

const FeatureCard = ({ icon: Icon, title, desc, delay }: any) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const scale = spring({ frame: frame - delay, fps, from: 0.8, to: 1, durationInFrames: 30, config: { damping: 12 } });
  const opacity = interpolate(frame - delay, [0, 15], [0, 1], { extrapolateRight: "clamp" });

  return (
    <div style={{ transform: `scale(${scale})`, opacity }} className="bg-white/5 border border-white/10 p-10 rounded-3xl w-80 flex flex-col items-center text-center backdrop-blur-md shadow-2xl">
      <div className="w-24 h-24 bg-brand-orange/20 rounded-full flex items-center justify-center mb-8">
        <Icon size={48} className="text-brand-orange" />
      </div>
      <h3 className="text-3xl font-bold mb-4">{title}</h3>
      <p className="text-xl text-gray-400 leading-relaxed text-balance">{desc}</p>
    </div>
  );
};

const HardwareScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const bgScale = spring({ frame, fps, from: 0.5, to: 1, durationInFrames: 40 });
  const bgOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });
  
  const exitX = interpolate(frame, [100, 120], [0, -1000], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill className="justify-center items-center" style={{ opacity: bgOpacity, transform: `translateX(${exitX}px)` }}>
      <div className="flex flex-col items-center max-w-5xl text-center">
        <div style={{ transform: `scale(${bgScale})` }} className="mb-12 relative">
          <div className="absolute inset-0 bg-brand-orange/30 blur-3xl rounded-full" />
          <Cpu size={120} className="text-white relative z-10" />
        </div>
        <h2 className="text-7xl font-bold mb-8 leading-tight">No Expensive Rigs Required.</h2>
        <p className="text-4xl text-gray-400 font-light text-balance leading-normal">
          Mineable with <span className="text-white font-bold">Arduinos</span>, <span className="text-white font-bold">ESP8266/ESP32</span>, and <span className="text-white font-bold">Raspberry Pis</span>.
        </p>
      </div>
    </AbsoluteFill>
  );
};

const CTAScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const enterX = spring({ frame, fps, from: 1000, to: 0, durationInFrames: 30, config: { damping: 14 } });
  const scale = spring({ frame: frame - 20, fps, from: 0.9, to: 1, durationInFrames: 30 });
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill className="justify-center items-center bg-brand-orange" style={{ transform: `translateX(${enterX}px)` }}>
      <div className="flex flex-col items-center" style={{ transform: `scale(${scale})`, opacity }}>
        <Img src={staticFile("images/brand/logo.png")} className="w-40 h-40 mb-12 drop-shadow-2xl brightness-0 invert" />
        <h2 className="text-8xl font-black mb-8 text-white tracking-tighter">Start Mining Today.</h2>
        <p className="text-4xl text-white/80 font-medium mb-16">Join the eco-friendly revolution.</p>
        
        <div className="bg-white text-brand-orange px-16 py-6 rounded-full text-3xl font-bold shadow-2xl hover:scale-105 transition-transform">
          duinocoin.com
        </div>
      </div>
    </AbsoluteFill>
  );
};
