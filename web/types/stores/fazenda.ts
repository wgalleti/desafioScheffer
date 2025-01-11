export interface iFazendaLinks {
    next: string | null;
    prev: string | null;
}

export interface iFazendaDados {
    id: string;
    nome: string;
    fardoes: number;
    rolinhos: number;
}

export interface iFazendaResponse {
    links: iFazendaLinks;
    total: number;
    data: iFazendaDados[];
}
