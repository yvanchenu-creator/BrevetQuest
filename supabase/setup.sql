-- BrevetQuest : base de données de la progression de Gabriel
-- À coller dans Supabase > SQL Editor > New query, puis cliquer sur "Run".

create table if not exists public.progress (
  code text primary key,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

-- Personne ne peut lire ou écrire la table directement :
alter table public.progress enable row level security;

-- On passe uniquement par ces deux fonctions, qui exigent le code famille.
create or replace function public.get_progress(p_code text)
returns jsonb language sql security definer set search_path = public as $$
  select data from public.progress where code = p_code and length(p_code) >= 12;
$$;

create or replace function public.save_progress(p_code text, p_data jsonb)
returns void language plpgsql security definer set search_path = public as $$
begin
  if length(p_code) < 12 then raise exception 'code trop court'; end if;
  insert into public.progress(code, data, updated_at) values (p_code, p_data, now())
  on conflict (code) do update set data = excluded.data, updated_at = now();
end;
$$;

grant execute on function public.get_progress(text) to anon;
grant execute on function public.save_progress(text, jsonb) to anon;
