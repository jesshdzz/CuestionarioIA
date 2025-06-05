import type { Metadata } from "next";
import "@/app/globals.css";

import { SideMenu } from "@/components/SideMenu";


export const metadata: Metadata = {
	title: "Cuestionario IA",
	description: "Un cuestionario para evaluar el conocimiento de programación utilizando IA",
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<div className="grid min-h-dvh grid-cols-[auto_1fr_auto]">
			<SideMenu />
			<main className="m-5 p-4">
				{children}
			</main>
		</div>
	);
}
