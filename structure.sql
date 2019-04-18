--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE "TestingSystem";
ALTER ROLE "TestingSystem" WITH SUPERUSER INHERIT NOCREATEROLE CREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'md5c1b8b6334f2f151f5d603632f6a16947';
CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md51ae4bafcbac11bcc0bb7f1ee182d9162';






--
-- Database creation
--

CREATE DATABASE "Tests" WITH TEMPLATE = template0 OWNER = "TestingSystem";
REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


\connect "Tests"

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7
-- Dumped by pg_dump version 10.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: bel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bel (
    id integer NOT NULL,
    name character varying(255),
    description text,
    answer text
);


ALTER TABLE public.bel OWNER TO postgres;

--
-- Name: bel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bel_id_seq OWNER TO postgres;

--
-- Name: bel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bel_id_seq OWNED BY public.bel.id;


--
-- Name: eng; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eng (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    answer text
);


ALTER TABLE public.eng OWNER TO postgres;

--
-- Name: eng_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.eng_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eng_id_seq OWNER TO postgres;

--
-- Name: eng_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.eng_id_seq OWNED BY public.eng.id;


--
-- Name: math; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.math (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    answer text NOT NULL
);


ALTER TABLE public.math OWNER TO postgres;

--
-- Name: math_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.math_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.math_id_seq OWNER TO postgres;

--
-- Name: math_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.math_id_seq OWNED BY public.math.id;


--
-- Name: rus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rus (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    answer text NOT NULL
);


ALTER TABLE public.rus OWNER TO postgres;

--
-- Name: rus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rus_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rus_id_seq OWNER TO postgres;

--
-- Name: rus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rus_id_seq OWNED BY public.rus.id;


--
-- Name: bel id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bel ALTER COLUMN id SET DEFAULT nextval('public.bel_id_seq'::regclass);


--
-- Name: eng id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eng ALTER COLUMN id SET DEFAULT nextval('public.eng_id_seq'::regclass);


--
-- Name: math id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.math ALTER COLUMN id SET DEFAULT nextval('public.math_id_seq'::regclass);


--
-- Name: rus id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rus ALTER COLUMN id SET DEFAULT nextval('public.rus_id_seq'::regclass);


--
-- Data for Name: bel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bel (id, name, description, answer) FROM stdin;
\.


--
-- Data for Name: eng; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eng (id, name, description, answer) FROM stdin;
\.


--
-- Data for Name: math; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.math (id, name, description, answer) FROM stdin;
\.


--
-- Data for Name: rus; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rus (id, name, description, answer) FROM stdin;
\.


--
-- Name: bel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bel_id_seq', 1, false);


--
-- Name: eng_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eng_id_seq', 1, false);


--
-- Name: math_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.math_id_seq', 1, false);


--
-- Name: rus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rus_id_seq', 1, false);


--
-- Name: eng eng_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eng
    ADD CONSTRAINT eng_name_key UNIQUE (name);


--
-- Name: math math_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.math
    ADD CONSTRAINT math_name_key UNIQUE (name);


--
-- Name: rus rus_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rus
    ADD CONSTRAINT rus_name_key UNIQUE (name);


--
-- PostgreSQL database dump complete
--

\connect postgres

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7
-- Dumped by pg_dump version 10.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: bel; Type: TABLE; Schema: public; Owner: TestingSystem
--

CREATE TABLE public.bel (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    answer text
);


ALTER TABLE public.bel OWNER TO "TestingSystem";

--
-- Name: bel_id_seq; Type: SEQUENCE; Schema: public; Owner: TestingSystem
--

CREATE SEQUENCE public.bel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bel_id_seq OWNER TO "TestingSystem";

--
-- Name: bel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: TestingSystem
--

ALTER SEQUENCE public.bel_id_seq OWNED BY public.bel.id;


--
-- Name: eng; Type: TABLE; Schema: public; Owner: TestingSystem
--

CREATE TABLE public.eng (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    answer text
);


ALTER TABLE public.eng OWNER TO "TestingSystem";

--
-- Name: eng_id_seq; Type: SEQUENCE; Schema: public; Owner: TestingSystem
--

CREATE SEQUENCE public.eng_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.eng_id_seq OWNER TO "TestingSystem";

--
-- Name: eng_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: TestingSystem
--

ALTER SEQUENCE public.eng_id_seq OWNED BY public.eng.id;


--
-- Name: math; Type: TABLE; Schema: public; Owner: TestingSystem
--

CREATE TABLE public.math (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    answer text
);


ALTER TABLE public.math OWNER TO "TestingSystem";

--
-- Name: math_id_seq; Type: SEQUENCE; Schema: public; Owner: TestingSystem
--

CREATE SEQUENCE public.math_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.math_id_seq OWNER TO "TestingSystem";

--
-- Name: math_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: TestingSystem
--

ALTER SEQUENCE public.math_id_seq OWNED BY public.math.id;


--
-- Name: rus; Type: TABLE; Schema: public; Owner: TestingSystem
--

CREATE TABLE public.rus (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    answer text
);


ALTER TABLE public.rus OWNER TO "TestingSystem";

--
-- Name: rus_id_seq; Type: SEQUENCE; Schema: public; Owner: TestingSystem
--

CREATE SEQUENCE public.rus_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rus_id_seq OWNER TO "TestingSystem";

--
-- Name: rus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: TestingSystem
--

ALTER SEQUENCE public.rus_id_seq OWNED BY public.rus.id;


--
-- Name: bel id; Type: DEFAULT; Schema: public; Owner: TestingSystem
--

ALTER TABLE ONLY public.bel ALTER COLUMN id SET DEFAULT nextval('public.bel_id_seq'::regclass);


--
-- Name: eng id; Type: DEFAULT; Schema: public; Owner: TestingSystem
--

ALTER TABLE ONLY public.eng ALTER COLUMN id SET DEFAULT nextval('public.eng_id_seq'::regclass);


--
-- Name: math id; Type: DEFAULT; Schema: public; Owner: TestingSystem
--

ALTER TABLE ONLY public.math ALTER COLUMN id SET DEFAULT nextval('public.math_id_seq'::regclass);


--
-- Name: rus id; Type: DEFAULT; Schema: public; Owner: TestingSystem
--

ALTER TABLE ONLY public.rus ALTER COLUMN id SET DEFAULT nextval('public.rus_id_seq'::regclass);


--
-- Data for Name: bel; Type: TABLE DATA; Schema: public; Owner: TestingSystem
--

COPY public.bel (id, name, description, answer) FROM stdin;
\.


--
-- Data for Name: eng; Type: TABLE DATA; Schema: public; Owner: TestingSystem
--

COPY public.eng (id, name, description, answer) FROM stdin;
\.


--
-- Data for Name: math; Type: TABLE DATA; Schema: public; Owner: TestingSystem
--

COPY public.math (id, name, description, answer) FROM stdin;
\.


--
-- Data for Name: rus; Type: TABLE DATA; Schema: public; Owner: TestingSystem
--

COPY public.rus (id, name, description, answer) FROM stdin;
\.


--
-- Name: bel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: TestingSystem
--

SELECT pg_catalog.setval('public.bel_id_seq', 1, false);


--
-- Name: eng_id_seq; Type: SEQUENCE SET; Schema: public; Owner: TestingSystem
--

SELECT pg_catalog.setval('public.eng_id_seq', 1, false);


--
-- Name: math_id_seq; Type: SEQUENCE SET; Schema: public; Owner: TestingSystem
--

SELECT pg_catalog.setval('public.math_id_seq', 1, false);


--
-- Name: rus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: TestingSystem
--

SELECT pg_catalog.setval('public.rus_id_seq', 1, false);


--
-- Name: bel bel_name_key; Type: CONSTRAINT; Schema: public; Owner: TestingSystem
--

ALTER TABLE ONLY public.bel
    ADD CONSTRAINT bel_name_key UNIQUE (name);


--
-- Name: eng eng_name_key; Type: CONSTRAINT; Schema: public; Owner: TestingSystem
--

ALTER TABLE ONLY public.eng
    ADD CONSTRAINT eng_name_key UNIQUE (name);


--
-- Name: math math_name_key; Type: CONSTRAINT; Schema: public; Owner: TestingSystem
--

ALTER TABLE ONLY public.math
    ADD CONSTRAINT math_name_key UNIQUE (name);


--
-- Name: rus rus_name_key; Type: CONSTRAINT; Schema: public; Owner: TestingSystem
--

ALTER TABLE ONLY public.rus
    ADD CONSTRAINT rus_name_key UNIQUE (name);


--
-- PostgreSQL database dump complete
--

\connect template1

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7
-- Dumped by pg_dump version 10.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

