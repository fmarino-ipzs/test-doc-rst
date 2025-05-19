Introduction
==========================

TEST single run workflow.

This document serves as an initial guide to the testing procedures employed for the automatic generation of technical documentation in pdf and html format. Within these pages, you will find a comprehensive overview of the testing strategy, encompassing the various levels and types of tests executed to ensure the quality and reliability of the software. The primary objective of this documentation is to provide stakeholders with a clear understanding of the testing efforts undertaken, the methodologies applied, and the expected outcomes. 
Furthermore, it aims to serve as a reference point for the testing team, outlining the processes and standards to be followed throughout the testing lifecycle.
This introductory section sets the stage for a more detailed exploration of the test environment, test cases, execution procedures, and reporting mechanisms that constitute the core of this document.

The following diagram depicts the High-Level Architecture.

.. plantuml:: plantuml/solution-architecture.puml
   :width: 100%
   :alt: The image illustrates the Solution and its relations and interactions within the ecosystem.
   :caption: Solution High Level Architecture


Requirements
------------

This section defines the main requirements ...

Below a non-normative example of the PAR.

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoid2FsbGV0LWF0dGVzdGF0aW9uK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJhYWwiOiJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIn19LCJhdXRob3JpemF0aW9uX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtc29sdXRpb24uZGlnaXRhbC1zdHJhdGVneS5ldXJvcGEuZXUvYXV0aG9yaXphdGlvbiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJyZXNwb25zZV9tb2Rlc19zdXBwb3J0ZWQiOlsiZm9ybV9wb3N0Lmp3dCJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJkYytzZC1qd3QiOnsic2Qtand0X2FsZ192YWx1ZXMiOlsiRVMyNTYiLCJFUzM4NCJdfX0sInJlcXVlc3Rfb2JqZWN0X3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXSwicHJlc2VudGF0aW9uX2RlZmluaXRpb25fdXJpX3N1cHBvcnRlZCI6ZmFsc2UsImNsaWVudF9pZF9zY2hlbWVzX3N1cHBvcnRlZCI6WyJlbnRpdHlfaWQiXSwiaWF0IjoxNzQwMTU4MDQ3LCJleHAiOjE3NDAxNTgxNjd9.paU3FOET8nraQxuesBXD9gw57DL5HfDzkeboKAOinyh5L2MmLwqvRtrSWK8S7qMRWYmdzR-gHMpmebIH7gGE5w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.eyJpc3MiOiIgaHR0cHM6Ly9jbGllbnQuZXhhbXBsZS5jb20iLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuY29tIiwianRpIjoiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwiaWF0IjoxNzQwMTU4NjE3LCJleHAiOjE3NDAxNTg3Mzd9.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-attestation$&
    request=$SIGNED-JWT


API
---
.. role:: raw-html(raw)
  :format: html

.. only:: html

   A complete OpenAPI Specification is available :raw-html:`<a href="API-test.html" target="_blank">here</a>`.

.. only:: latex

   A complete OpenAPI Specification is included in :ref:`appendix:Appendix A - OpenAPI Specification`.

