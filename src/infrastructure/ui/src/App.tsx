import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import axios from 'axios';

interface DiceFace {
  number: number;
  pattern: string[];
}

function App() {
  const [diceFace, setDiceFace] = useState<DiceFace | null>(null);
  const [isRolling, setIsRolling] = useState(false);

  const rollDice = async () => {
    setIsRolling(true);
    try {
      const response = await axios.get('http://localhost:8000/api/roll');
      setDiceFace(response.data);
    } catch (error) {
      console.error('Error rolling dice:', error);
    }
    setTimeout(() => setIsRolling(false), 1000);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg">
        <h1 className="text-3xl font-bold text-center mb-8">サイコロゲーム</h1>
        
        <motion.div
          className="mb-8"
          animate={{
            rotate: isRolling ? [0, 360] : 0,
            scale: isRolling ? [1, 1.2, 1] : 1,
          }}
          transition={{ duration: 0.5 }}
        >
          {diceFace && (
            <div className="font-mono text-center">
              {diceFace.pattern.map((line, index) => (
                <div key={index}>{line}</div>
              ))}
            </div>
          )}
        </motion.div>

        <button
          onClick={rollDice}
          disabled={isRolling}
          className={`w-full py-3 px-6 rounded-lg text-white font-bold
            ${isRolling 
              ? 'bg-gray-400 cursor-not-allowed' 
              : 'bg-blue-500 hover:bg-blue-600'
            }`}
        >
          {isRolling ? 'サイコロを振っています...' : 'サイコロを振る'}
        </button>
      </div>
    </div>
  );
}

export default App; 