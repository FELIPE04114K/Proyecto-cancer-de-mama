import Header from "../components/Header";
import Footer from "../components/Footer";

export default function Home() {
  return (
    
    <div className="min-h-screen w-full flex flex-col pt-0">
      <Header />

      <main 
        className="flex-grow flex items-center justify-center bg-cover bg-center bg-no-repeat w-full min-h-screen"
        style={{ backgroundImage: `url('/cancer.jpg')`}}
        >
        <section className="flex flex-col items-center px-4 py-10">
        <div className="bg-white/70 p-8 rounded-2xl shadow-lg max-w-3xl text-center z-10">
            
            <h1 className="text-3xl md:text-4xl font-bold text-pink-700 mb-6">
                🎀 Bienvenida a la App de Cáncer de Mama
            </h1>

            <p className="text-gray-700 font-bold text-lg">
                Esta aplicación te ayudará a visualizar síntomas, explorar estadísticas
                y conocer mejor los indicadores previos al diagnóstico de cáncer de mama.
            </p>

            <a href="/sintomas">
              <button type="button" className="mt-6 bg-pink-700 text-white px-4 py-2 rounded-lg hover:bg-pink-600 transition duration-300">
                Elegir Síntomas
              </button>
            </a>
        </div>

        {/* <div className="absolute inset-0 bg-white bg-opacity-30"></div> */}

        </section>

      </main>
     <Footer />
    </div>
  );
}