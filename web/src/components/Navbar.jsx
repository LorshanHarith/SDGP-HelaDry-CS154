import React from "react";

function Navbar() {
  return (
    <nav className="flex justify-between items-center p-4 bg-green-700 text-white">
      
      <div className="flex items-center gap-2">
        <img src="/logo.png" alt="HelaDry Logo" className="w-10"/>
        <h1 className="text-xl font-bold">HelaDry</h1>
      </div>

      <ul className="flex gap-6">
        <li className="cursor-pointer hover:text-yellow-300">Home</li>
        <li className="cursor-pointer hover:text-yellow-300">About</li>
        <li className="cursor-pointer hover:text-yellow-300">Features</li>
        <li className="cursor-pointer hover:text-yellow-300">Team</li>
        <li className="cursor-pointer hover:text-yellow-300">Contact</li>
      </ul>

    </nav>
  );
}

export default Navbar;