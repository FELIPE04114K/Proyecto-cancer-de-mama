import { useState } from 'react';

export default function Header() {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className='bg-pink-700 text-white p-4 shadow-md w-full fixed top-0 left-0 z-10'>
            <div className='container mx-auto flex items-center justify-between'>
                <a href="/">
                    <h1 className='text-2xl font-bold'>Cáncer de Mama</h1>
                </a>

                <div className='hidden md:flex space-x-6'>
                    <a href="/" className='hover:underline'>Inicio</a>
                    <a href="/sintomas" className='hover:underline'>Síntomas</a>
                    
                    <a href="https://github.com/FELIPE04114K/Proyecto-cancer-de-mama" target="_blank" className='hover:underline'>Github</a>
                </div>

                {/* Mobile Menu Button */}
                <button
                    className='md:hidden'
                    onClick={() => setIsOpen(!isOpen)}
                    aria-label="Abrir menú"
                >
                    ☰
                </button>
            </div>

            {/* Mobile Menu */}
            {isOpen && (
            <div className='md:hidden flex flex-col items-start px-4 mt-2 space-y-2'>
                <a href="#">Inicio</a>
                <a href="#">Síntomas</a>
                <a href="#">Estadísticas</a>
                <a href="#">Github</a>
            </div>
            )}
        </nav>
    );
}