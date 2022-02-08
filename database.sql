--
-- PostgreSQL database dump
--

-- Dumped from database version 14.0
-- Dumped by pg_dump version 14.0

-- Started on 2022-02-07 14:47:01 MST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 73415)
-- Name: shoes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shoes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    size integer NOT NULL,
    side text NOT NULL,
    brand text NOT NULL,
    style text NOT NULL,
    description text NOT NULL,
    image_url text NOT NULL
);


ALTER TABLE public.shoes OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 73408)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name text NOT NULL,
    email text NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 3579 (class 0 OID 73415)
-- Dependencies: 210
-- Data for Name: shoes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shoes (id, user_id, size, side, brand, style, description, image_url) FROM stdin;
\.


--
-- TOC entry 3578 (class 0 OID 73408)
-- Dependencies: 209
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, email) FROM stdin;
\.


--
-- TOC entry 3437 (class 2606 OID 73421)
-- Name: shoes shoes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shoes
    ADD CONSTRAINT shoes_pkey PRIMARY KEY (id);


--
-- TOC entry 3435 (class 2606 OID 73414)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3438 (class 2606 OID 73422)
-- Name: shoes users_shoes; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shoes
    ADD CONSTRAINT users_shoes FOREIGN KEY (user_id) REFERENCES public.users(id) NOT VALID;


-- Completed on 2022-02-07 14:47:01 MST

--
-- PostgreSQL database dump complete
--

