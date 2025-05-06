import React, { useState } from 'react';
import Footer from '../components/Footer';
import Header from '../components/Header';
import Bentos from '../components/Bentos';
// opcional si quieres imagen de fondo
// import sintomasBg from '../assets/sintomas-bg.png'; // opcional si quieres imagen de fondo

const sintomasDisponibles = [
  { id: 'bulto', nombre: 'Bulto en el seno' },
  { id: 'dolor', nombre: 'Dolor persistente' },
  { id: 'pezon', nombre: 'Cambios en el pezón' },
  { id: 'piel', nombre: 'Cambios en la piel del seno' },
];

export default function Sintomas() {
  const [seleccionados, setSeleccionados] = useState([]);
  const [resultados, setResultados] = useState([]);

  const manejarCambio = (id, valor) => {
    setSeleccionados(prev =>
      prev.some(item => item.id === id)
        ? prev.map(item => item.id === id ? { ...item, valor } : item)
        : [...prev, { id, valor }]
    );
  };

  const enviarAlBackend = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/sintomas', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(seleccionados),
      });

      const data = await response.json();
      setResultados(data); // data: array de objetos con {graficoUrl, explicacion}
    } catch (error) {
      console.error('Error al enviar al backend:', error);
    }
  };

  return (
      <div className="min-h-screen w-full flex flex-col">
        <Header />
      {/* Formulario de selección */}
      <main className="flex-grow flex flex-col items-center text-center justify-between px-4 py-38">
        <h1 className="text-4xl font-bold text-pink-700 mb-6">Selecciona tus síntomas</h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-3xl">
          {sintomasDisponibles.map(sintoma => (
            <div key={sintoma.id} className="bg-white bg-opacity-90 p-4 rounded-xl shadow">
              <label className="block text-gray-800 font-semibold mb-2">{sintoma.nombre}</label>
              <select
                onChange={e => manejarCambio(sintoma.id, e.target.value)}
                className="w-full p-2 rounded border border-gray-300"
                defaultValue=""
              >
                <option value="" disabled>Selecciona intensidad</option>
                <option value="leve">Leve</option>
                <option value="moderado">Moderado</option>
                <option value="severo">Severo</option>
              </select>
            </div>
          ))}
        </div>

        <button
          onClick={enviarAlBackend}
          className="mt-8 bg-pink-700 text-white px-6 py-3 rounded-xl hover:bg-pink-800 transition"
        >
          Enviar al análisis
        </button>
      </main>

      {/* Resultados en formato bento */}
      {resultados.length > 0 && (
        <section className="px-4 py-10 bg-white">
          <h2 className="text-2xl font-bold text-center text-pink-700 mb-8">
            Resultados del análisis
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
            {resultados.map((res, index) => (
              <div key={index} className="bg-pink-50 p-4 rounded-2xl shadow-lg">
                <img
                  src={res.graficoUrl}
                  alt={`Gráfico ${index + 1}`}
                  className="w-full h-48 object-contain mb-4"
                />
                <p className="text-gray-700 text-sm">{res.explicacion}</p>
              </div>
            ))}
          </div>
        </section>
      )}

        {resultados.length > 0 && (
            <>
                <h2 className="text-2xl font-bold text-center text-pink-700 mt-10">Resultados del análisis</h2>
                <BentoGrid resultados={resultados} />
            </>
        )}

      <Footer />
    </div>
  );
}
