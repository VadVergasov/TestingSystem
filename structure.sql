--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

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

