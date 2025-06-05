import Link from "next/link";
import { ReactElement } from "react";

export const ElementoMenu = ({ href, texto, icono }: { href: string, texto: string, icono: ReactElement }) => {
    return (
        <div className="w-full h-10">
            <Link href={href} className="group relative flex justify-center rounded-sm px-2 py-1.5 text-gray-500 hover:bg-gray-50 hover:text-gray-700">
                {icono}
                <span className="invisible absolute start-full top-1/2 ms-4 -translate-y-1/2 rounded-sm bg-gray-900 px-2 py-1.5 text-xs font-medium text-white group-hover:visible" >
                    {texto}
                </span>
            </Link>
        </div>
    );
}