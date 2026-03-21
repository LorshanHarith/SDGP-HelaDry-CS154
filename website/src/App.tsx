import React from 'react';
import Navbar from './components/UI/Navbar';
import LoadingScreen from './components/UI/LoadingScreen';
import CanvasScrollSequence from './components/Hero/CanvasScrollSequence';
import Mission from './components/Sections/Mission';
import Technology from './components/Sections/Technology';
import Team from './components/Sections/Team';
import Footer from './components/UI/Footer';

function App() {
  return (
    <div className="antialiased selection:bg-primary selection:text-white">
      {/* High-end White and Green Loading Screen */}
      <LoadingScreen />

      {/* Navigation Bar: Fades in after the zoom sequence */}
      <Navbar />

      <main className="relative overflow-x-hidden">
        {/* Hero Section: Cinematic Scroll-Scrub Animation */}
        <section id="hero" className="relative bg-black">
          <CanvasScrollSequence />
        </section>

        {/* Content Sections: High-contrast White/Green Layout */}
        <Mission />

        <Technology />

        <Team />

        {/* Additional placeholder sections to demonstrate scroll depth */}
        <section id="impact" className="h-screen bg-white flex items-center justify-center text-black">
          <h2 className="text-6xl font-heading text-primary">Global Impact</h2>
        </section>

        <Footer />
      </main>
    </div>
  );
}

export default App;
