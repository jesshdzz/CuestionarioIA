import { FaRegUserCircle, FaHome } from "react-icons/fa";
import { MdLogout } from "react-icons/md";
import { RiSurveyLine } from "react-icons/ri";

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
        icono: <RiSurveyLine size={28} />
    }
]


export const SideMenu = () => {
    return (
        <div className="flex h-screen w-24 flex-col justify-between border-e border-base-200 bg-base-300">
            <div>
                <div className="flex flex-row items-center justify-center p-3">
                    <span className="grid size-16 place-content-center rounded-lg bg-base-100 text-xs text-gray-600">
                        L
                    </span>
                </div>

                <div className="px-2">
                    <div className="py-4 border-t border-base-100">
                        <ElementoMenu
                            href="/perfil"
                            texto="Perfil"
                            icono={<FaRegUserCircle size={28} />}
                        />
                    </div>

                    <div className="grid gap-3 grid-cols-1 border-t border-base-100 py-4">
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

            <div className="sticky inset-x-0 bottom-0 bg-base-300 p-2">
                <div className="border-t border-base-100">
                    <ElementoMenu href="/logout" texto="cerrar sesión" icono={<MdLogout size={28} />} />

                </div>
                <div className="flex items-center justify-center mt-2">
                    <input type="checkbox" value="dracula" className="toggle theme-controller" />
                </div>

            </div>
        </div>
    )

}