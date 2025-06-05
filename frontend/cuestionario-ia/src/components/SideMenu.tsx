import { FaRegUserCircle, FaHome } from "react-icons/fa";
import { MdLogout } from "react-icons/md";
import { FcSurvey } from "react-icons/fc";

import { ElementoMenu } from "./ElementoMenu";

const elementos = [
    {
        href: "/incio",
        texto: "Inicio",
        icono: <FaHome size={28} />
    },
    {
        href: "/cuestionario",
        texto: "Cuestionario",
        icono: <FcSurvey size={28} />
    }
]


export const SideMenu = () => {
    return (
        <div className="flex h-screen w-24 flex-col justify-between border-e border-gray-100 bg-white">
            <div>
                <div className="flex flex-row items-center justify-center p-3">
                    <span className="grid size-16 place-content-center rounded-lg bg-gray-100 text-xs text-gray-600">
                        L
                    </span>
                </div>

                <div className="border-t border-gray-100">
                    <div className="px-2">
                        <div className="py-4">
                            <ElementoMenu
                                href="/perfil"
                                texto="Perfil"
                                icono={<FaRegUserCircle size={28} />}
                            />
                        </div>

                        <div className="grid gap-3 grid-cols-1 border-t border-gray-100 py-4">
                            {elementos.map((elemento, index) => (
                                <ElementoMenu
                                    key={index}
                                    href={elemento.href}
                                    texto={elemento.texto}
                                    icono={elemento.icono}
                                />
                            ))}
                        </div>
                    </div>
                </div>
            </div>
            <div className="sticky inset-x-0 bottom-0 border-t border-gray-100 bg-white p-2">
                <ElementoMenu href="/logout" texto="cerrar sesión" icono={<MdLogout size={28} />} />
                <div className="flex items-center justify-center mt-2">
                    <input type="checkbox" value="dracula" className="toggle theme-controller" />
                </div>

            </div>
        </div>
    )

}