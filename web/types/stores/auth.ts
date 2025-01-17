export interface iAuthStore {
  user: string | null;
  token: string | null;
  isLoggedIn: boolean;
}

export interface iAuthCredenciais {
  username: string;
  password: string;
}

export interface iAuthUser {
  username: string;
  email: string;
}

export interface iAuthResponse {
  token: string | null;
  user: iAuthUser | null;
  refresh: string | null;
}
