CREATE TABLE public.user (
    id serial NOT NULL,
    name varchar(256) NOT NULL,
    PRIMARY KEY (id))
;

CREATE TABLE public.damndaily (
    at timestamp with time zone NULL,
    created timestamp with time zone NULL,
    deleted timestamp with time zone NULL,
    id serial NOT NULL,
    location varchar(1024) NULL,
    name varchar(512) NOT NULL,
    PRIMARY KEY (id))
;

CREATE TABLE public.today (
    at timestamp with time zone NULL,
    damndaily_id integer NOT NULL,
    id serial NOT NULL,
    location varchar(256) NULL,
    PRIMARY KEY (id))
;

CREATE TABLE public.participation (
    today_id integer NOT NULL,
    user_id integer NOT NULL,
    PRIMARY KEY (today_id, user_id))
;

CREATE TABLE public.message (
    id serial NOT NULL,
    today_id integer NOT NULL,
    user_id integer NOT NULL,
    value varchar(1024) NOT NULL,
    PRIMARY KEY (id))
;

ALTER TABLE public.today ADD FOREIGN KEY (damndaily_id) REFERENCES public.damndaily (id);
ALTER TABLE public.participation ADD FOREIGN KEY (today_id) REFERENCES public.today (id);
ALTER TABLE public.participation ADD FOREIGN KEY (user_id) REFERENCES public.user (id);
ALTER TABLE public.message ADD FOREIGN KEY (today_id) REFERENCES public.today (id);
ALTER TABLE public.message ADD FOREIGN KEY (user_id) REFERENCES public.user (id);

