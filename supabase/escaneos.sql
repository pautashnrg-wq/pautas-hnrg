-- Registro de escaneos de las fichas (Pautas HNRG).
-- Pegar en Supabase > SQL Editor > Run.

create table if not exists public.escaneos (
  id         bigint generated always as identity primary key,
  tema       text not null check (char_length(tema) between 1 and 50),
  origen     text not null check (origen in ('nfc', 'qr', 'directo')),
  user_agent text check (char_length(user_agent) <= 300),
  creado_en  timestamptz not null default now()
);

alter table public.escaneos enable row level security;

-- Anónimos: solo pueden insertar. Sin política de select/update/delete,
-- la lectura queda bloqueada desde la web (se lee desde el panel de Supabase).
drop policy if exists "insertar escaneos anonimo" on public.escaneos;
create policy "insertar escaneos anonimo"
  on public.escaneos for insert
  to anon
  with check (true);

revoke all on public.escaneos from anon, authenticated;
grant insert on public.escaneos to anon;
