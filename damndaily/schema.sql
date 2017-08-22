--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.3
-- Dumped by pg_dump version 9.6.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: damndaily; Type: TABLE; Schema: public; Owner: damn
--

CREATE TABLE damndaily (
    id integer NOT NULL,
    name character varying(512) NOT NULL,
    created timestamp with time zone,
    deleted timestamp with time zone,
    location character varying(1024),
    at timestamp with time zone
);


ALTER TABLE damndaily OWNER TO damn;

--
-- Name: damndaily_id_seq; Type: SEQUENCE; Schema: public; Owner: damn
--

CREATE SEQUENCE damndaily_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE damndaily_id_seq OWNER TO damn;

--
-- Name: damndaily_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: damn
--

ALTER SEQUENCE damndaily_id_seq OWNED BY damndaily.id;


--
-- Name: message; Type: TABLE; Schema: public; Owner: damn
--

CREATE TABLE message (
    id integer NOT NULL,
    value character varying(1024) NOT NULL,
    today_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE message OWNER TO damn;

--
-- Name: message_id_seq; Type: SEQUENCE; Schema: public; Owner: damn
--

CREATE SEQUENCE message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE message_id_seq OWNER TO damn;

--
-- Name: message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: damn
--

ALTER SEQUENCE message_id_seq OWNED BY message.id;


--
-- Name: participation; Type: TABLE; Schema: public; Owner: damn
--

CREATE TABLE participation (
    today_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE participation OWNER TO damn;

--
-- Name: today; Type: TABLE; Schema: public; Owner: damn
--

CREATE TABLE today (
    id integer NOT NULL,
    location character varying(256),
    at timestamp with time zone,
    damndaily_id integer NOT NULL
);


ALTER TABLE today OWNER TO damn;

--
-- Name: today_id_seq; Type: SEQUENCE; Schema: public; Owner: damn
--

CREATE SEQUENCE today_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE today_id_seq OWNER TO damn;

--
-- Name: today_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: damn
--

ALTER SEQUENCE today_id_seq OWNED BY today.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: damn
--

CREATE TABLE "user" (
    id integer NOT NULL,
    name character varying(256) NOT NULL
);


ALTER TABLE "user" OWNER TO damn;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: damn
--

CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE user_id_seq OWNER TO damn;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: damn
--

ALTER SEQUENCE user_id_seq OWNED BY "user".id;


--
-- Name: damndaily id; Type: DEFAULT; Schema: public; Owner: damn
--

ALTER TABLE ONLY damndaily ALTER COLUMN id SET DEFAULT nextval('damndaily_id_seq'::regclass);


--
-- Name: message id; Type: DEFAULT; Schema: public; Owner: damn
--

ALTER TABLE ONLY message ALTER COLUMN id SET DEFAULT nextval('message_id_seq'::regclass);


--
-- Name: today id; Type: DEFAULT; Schema: public; Owner: damn
--

ALTER TABLE ONLY today ALTER COLUMN id SET DEFAULT nextval('today_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: damn
--

ALTER TABLE ONLY "user" ALTER COLUMN id SET DEFAULT nextval('user_id_seq'::regclass);


--
-- Data for Name: damndaily; Type: TABLE DATA; Schema: public; Owner: damn
--

COPY damndaily (id, name, created, deleted, location, at) FROM stdin;
\.


--
-- Name: damndaily_id_seq; Type: SEQUENCE SET; Schema: public; Owner: damn
--

SELECT pg_catalog.setval('damndaily_id_seq', 1, false);


--
-- Data for Name: message; Type: TABLE DATA; Schema: public; Owner: damn
--

COPY message (id, value, today_id, user_id) FROM stdin;
\.


--
-- Name: message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: damn
--

SELECT pg_catalog.setval('message_id_seq', 1, false);


--
-- Data for Name: participation; Type: TABLE DATA; Schema: public; Owner: damn
--

COPY participation (today_id, user_id) FROM stdin;
\.


--
-- Data for Name: today; Type: TABLE DATA; Schema: public; Owner: damn
--

COPY today (id, location, at, damndaily_id) FROM stdin;
\.


--
-- Name: today_id_seq; Type: SEQUENCE SET; Schema: public; Owner: damn
--

SELECT pg_catalog.setval('today_id_seq', 1, false);


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: damn
--

COPY "user" (id, name) FROM stdin;
\.


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: damn
--

SELECT pg_catalog.setval('user_id_seq', 1, false);


--
-- Name: damndaily damndaily_pkey; Type: CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY damndaily
    ADD CONSTRAINT damndaily_pkey PRIMARY KEY (id);


--
-- Name: message message_pkey; Type: CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY message
    ADD CONSTRAINT message_pkey PRIMARY KEY (id);


--
-- Name: participation participation_pkey; Type: CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY participation
    ADD CONSTRAINT participation_pkey PRIMARY KEY (today_id, user_id);


--
-- Name: today today_pkey; Type: CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY today
    ADD CONSTRAINT today_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: today damndaily_fk; Type: FK CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY today
    ADD CONSTRAINT damndaily_fk FOREIGN KEY (damndaily_id) REFERENCES damndaily(id) ON DELETE CASCADE;


--
-- Name: participation today_fk; Type: FK CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY participation
    ADD CONSTRAINT today_fk FOREIGN KEY (today_id) REFERENCES today(id);


--
-- Name: message today_fk; Type: FK CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY message
    ADD CONSTRAINT today_fk FOREIGN KEY (today_id) REFERENCES today(id);


--
-- Name: participation user_fk; Type: FK CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY participation
    ADD CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES "user"(id);


--
-- Name: message user_fk; Type: FK CONSTRAINT; Schema: public; Owner: damn
--

ALTER TABLE ONLY message
    ADD CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES "user"(id);


--
-- PostgreSQL database dump complete
--

