import React from 'react';

export default function BentoGrid({ resultados }) {
  return (
    <div className="grid grid-cols-3 gap-4 max-w-6xl mx-auto px-4 py-10">
      {resultados.map((item, index) => (
        <React.Fragment key={index}>
          {/* GRAFICA - ocupa 2 columnas */}
          <div className="col-span-2 bg-green-100 p-4 rounded-xl shadow-md flex items-center justify-center">
            <img src={item.graficoUrl} alt={`Gráfico ${index + 1}`} className="h-48 object-contain" />
          </div>

          {/* EXPLICACIÓN - ocupa 1 columna */}
          <div className="bg-green-300 p-4 rounded-xl shadow-md text-sm flex items-center justify-center">
            {item.explicacion}
          </div>
        </React.Fragment>
      ))}
    </div>
  );
}
