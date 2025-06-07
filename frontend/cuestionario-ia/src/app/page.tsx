"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
    const router = useRouter();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleLogin = async () => {
        try {
            const res = await fetch("http://localhost:8001/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email, password }),
            });

            if (res.ok) {
                const data = await res.json();
                localStorage.setItem("token", data.access_token);
                router.push("/dashboard"); // redirige a dashboard o página protegida
            } else {
                const error = await res.json();
                throw new Error(error.message || "Error al iniciar sesión");
            }
        } catch (err: unknown) {
            setError(err instanceof Error ? err.message : "Ocurrió un error desconocido");
        }
    };

    return (
        <div className="container mx-auto py-24 px-6 h-dvh">
            <div className="max-w-md mx-auto px-6">
                <div className="p-6 flex flex-col items-center justify-center gap-5">
                    <h1 className="text-2xl font-bold text-center">
                        Bienvenido!
                    </h1>
                    {error && (
                        <div className="alert alert-error shadow-lg w-full">
                            <div>
                                <span>{error}</span>
                            </div>
                        </div>
                    )}
                    <fieldset className="fieldset bg-orange-100 border border-base-300 w-full px-4 py-8 shadow-lg rounded-box gap-6">
                        <label className="floating-label">
                            <input
                                className="input input-md validator"
                                type="email"
                                required
                                placeholder="correo@sitio.com"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                            <div className="validator-hint hidden">Ingresa un correo electronico valido</div>
                            <span className="">Correo</span>
                        </label>
                        <label className="floating-label" tabIndex={0}>
                            <input
                                className="input input-md validator"
                                type="password"
                                required
                                placeholder="Contraseña"
                                minLength={8}
                                pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                            <p className="validator-hint hidden">
                                Debe contener al menos 8 caracteres, incluyendo:
                                <br />Al menos un dígito
                                <br />Al menos una letra minúscula
                                <br />Al menos una letra mayúscula
                            </p>
                            <span>Contraseña</span>
                        </label>
                        <button
                            className="btn btn-neutral mt-4"
                            onClick={handleLogin}>
                            Iniciar Sesión
                        </button>
                        <p className="text-sm text-gray-500 text-center">
                            ¿No tienes una cuenta? <a href="/registro" className="text-blue-500 hover:underline">Regístrate</a>
                        </p>
                    </fieldset>
                </div>
            </div >
        </div >
    );
}
