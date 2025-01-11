export interface iAuthStore {
  user: string | null;
  token: string | null;
  isLoggedIn: boolean;
}

export interface iAuthCredenciais {
  username: string;
  password: string;
}

export interface iAuthResponse {
  token: string | null;
  refresh: string | null;
}
