export default function Home() {
    return (
        <div className="container mx-auto py-24 px-6 h-dvh">
            <div className="max-w-md mx-auto px-6">
                <div className="p-6 flex flex-col items-center justify-center gap-5">
                    <h1 className="text-2xl font-bold text-center">
                        Bienvenido!
                    </h1>
                    <fieldset className="fieldset bg-orange-100 border border-base-300 w-full px-4 py-8 shadow-lg rounded-box gap-6">
                        <label className="floating-label">
                            <input type="email" className="input input-md validator" required placeholder="correo@sitio.com" />
                            <div className="validator-hint hidden">Ingresa un correo electronico valido</div>
                            <span className="">Correo</span>
                        </label>
                        <label className="floating-label" tabIndex={0}>
                            <input type="password" className="input input-md validator" required placeholder="Contraseña" minLength={8} pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"/>
                            <p className="validator-hint hidden">
                                Debe contener al menos 8 caracteres, incluyendo:
                                <br />Al menos un dígito
                                <br />Al menos una letra minúscula
                                <br />Al menos una letra mayúscula
                            </p>
                            <span>Contraseña</span>
                        </label>
                        <button className="btn btn-neutral mt-4">Iniciar Sesión</button>
                        <p className="text-sm text-gray-500 text-center">
                            ¿No tienes una cuenta? <a href="/registro" className="text-blue-500 hover:underline">Regístrate</a>
                        </p>
                    </fieldset>
                </div>
            </div >
        </div >
    );
}
