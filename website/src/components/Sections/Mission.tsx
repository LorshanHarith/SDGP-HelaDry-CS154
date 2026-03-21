/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { motion } from 'motion/react';

export default function Mission() {
  return (
    <section id="mission" className="relative z-10 bg-white py-32 px-6 overflow-hidden">
      <motion.div 
        initial={{ opacity: 0, y: 100 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
        viewport={{ once: true, margin: "-20%" }}
        className="max-w-7xl mx-auto"
      >
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
          {/* Text Content */}
          <motion.div 
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            viewport={{ once: true }}
            className="space-y-10"
          >
            <div className="space-y-4">
              <span className="text-primary font-bold tracking-[0.3em] uppercase text-xs">Our Core Mission</span>
              <h2 className="text-6xl md:text-8xl font-heading text-black leading-[0.9] tracking-tighter">
                Harvesting <br />
                <span className="text-primary italic">Pure Energy.</span>
              </h2>
            </div>
            
            <p className="text-xl text-gray-500 font-body leading-relaxed max-w-xl">
              Heladry is at the forefront of sustainable agriculture. We design and deploy advanced solar dehydration systems that preserve nutritional value while eliminating post-harvest waste.
            </p>

            <div className="flex flex-col sm:flex-row gap-6 pt-6">
              <button className="bg-primary text-white px-12 py-6 rounded-full font-bold text-lg hover:bg-primary-dark transition-all shadow-xl shadow-primary/20">
                The Technology
              </button>
              <button className="border-2 border-gray-200 text-black px-12 py-6 rounded-full font-bold text-lg hover:border-primary hover:text-primary transition-all">
                View Impact
              </button>
            </div>
          </motion.div>

          {/* Image / Visual */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1, ease: "easeOut" }}
            viewport={{ once: true }}
            className="relative"
          >
            <div className="aspect-[4/5] rounded-[3rem] overflow-hidden shadow-2xl relative z-10">
              <img 
                src="https://picsum.photos/seed/heladry-mission/1200/1500" 
                alt="Solar Dehydrator in action" 
                className="w-full h-full object-cover"
                referrerPolicy="no-referrer"
              />
              {/* Floating Badge */}
              <div className="absolute bottom-10 left-10 bg-white/90 backdrop-blur-md p-8 rounded-3xl shadow-2xl border border-white/20 max-w-[240px]">
                <p className="text-primary font-black text-4xl leading-none">95%</p>
                <p className="text-gray-600 text-sm font-bold mt-2 uppercase tracking-wider">Efficiency Increase in drying time</p>
              </div>
            </div>
            
            {/* Background Decorative Element */}
            <div className="absolute -top-20 -right-20 w-64 h-64 bg-primary/5 rounded-full blur-3xl" />
            <div className="absolute -bottom-20 -left-20 w-96 h-96 bg-primary/10 rounded-full blur-3xl" />
          </motion.div>
        </div>
      </motion.div>
    </section>
  );
}
