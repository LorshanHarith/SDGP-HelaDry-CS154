/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { motion, AnimatePresence } from 'motion/react';
import { useEffect, useState } from 'react';
import { Sun } from 'lucide-react';

/**
 * LoadingScreen: A high-end White and Green intro.
 * Displays our logo and a Green Title with a modern "Hook" subtext below it.
 * Using the specified fonts: Plus Jakarta Sans (Headings) and Inter (Body).
 */
export default function LoadingScreen() {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulate initial asset loading
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 2500);

    return () => clearTimeout(timer);
  }, []);

  return (
    <AnimatePresence>
      {isLoading && (
        <motion.div
          initial={{ opacity: 1 }}
          exit={{ opacity: 0, y: -100 }}
          transition={{ duration: 0.8, ease: [0.76, 0, 0.24, 1] }}
          className="fixed inset-0 z-[9999] flex flex-col items-center justify-center bg-white"
        >
          <div className="relative flex flex-col items-center space-y-8">
            {/* Logo Animation */}
            <motion.div
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 1, ease: 'easeOut' }}
              className="w-32 h-32 bg-primary rounded-3xl flex items-center justify-center shadow-2xl"
            >
              <Sun className="w-20 h-20 text-white" />
            </motion.div>

            {/* Title and Hook */}
            <div className="text-center space-y-2">
              <motion.h1
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.5, duration: 0.8 }}
                className="text-4xl md:text-6xl font-heading font-extrabold text-primary tracking-tight"
              >
                HELADRY
              </motion.h1>
              <motion.p
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.8, duration: 0.8 }}
                className="text-lg md:text-xl font-body text-gray-500 italic"
              >
                Empowering the Future, One Ray at a Time.
              </motion.p>
            </div>

            {/* Progress Bar */}
            <motion.div
              initial={{ scaleX: 0 }}
              animate={{ scaleX: 1 }}
              transition={{ delay: 0.2, duration: 2, ease: 'easeInOut' }}
              className="absolute -bottom-16 w-48 h-1 bg-primary origin-left rounded-full"
            />
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}