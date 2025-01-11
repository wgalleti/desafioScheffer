export interface iAlgodoeiraLinks {
    next: string | null;
    prev: string | null;
}

export interface iAlgodoeiraDados {
    id: string;
    nome: string;
    producao: number;
}

export interface iAlgodoeiraResponse {
    links: iAlgodoeiraLinks;
    total: number;
    data: iAlgodoeiraDados[];
}
