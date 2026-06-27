#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:39:29 2026

@author: a
"""
import unittest
from unittest.mock import patch
import io
import sys
# Importamos las funciones y variables de tu programa principal
from smart_match import ( usuarios, registrar_candidato, menu_principal)


class TestSmartMatching(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba para limpiar la base de datos simulada."""
        usuarios.clear()
     
    # --- PRUEBA 1: Registro de Candidato Duplicado ---
    @patch('builtins.input', side_effect=['test@ccc.com', 'Jesus Arturo', 'Inglés', '10000', 'test@ccc.com'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_registro_duplicado(self, mock_stdout, mock_input):
        # Ejecutamos el primer registro (exitoso)
        registrar_candidato()

        # Ejecutamos el segundo registro (intento de duplicado)
        registrar_candidato()

        # Obtenemos todo lo que el programa imprimió en la consola
        salida_consola = mock_stdout.getvalue()

        # Validamos que el sistema detectó el duplicado
        self.assertIn("Error: El usuario ya está registrado.", salida_consola)
        # Validamos que solo exista un registro con ese correo en la base de datos
        self.assertEqual(len(usuarios), 1)

    # --- PRUEBA 2: Manejo de Mayúsculas en Búsqueda de Vacantes ---
    @patch('builtins.input', side_effect=['ana@ccc.com', 'Ana', 'inglés', '15000'])
    def test_manejo_mayusculas(self, mock_input):
        # Ejecutamos el registro ingresando "inglés" en minúsculas
        registrar_candidato()

        # Validamos que el método .capitalize() hizo su trabajo internamente
        # y guardó el dato como "Inglés"
        idioma_guardado = usuarios['ana@ccc.com']['idioma']
        self.assertEqual(idioma_guardado, "Inglés")
         
    # --- PRUEBA 3: Condición de Salida del Sistema ---
    @patch('builtins.input', side_effect=['6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_salida_sistema(self, mock_stdout, mock_input):
        # Al ingresar "6", el menú debería terminar sin errores y mostrar el mensaje de salida
        menu_principal()
        salida_consola = mock_stdout.getvalue()
        
        # Corregido: Esta línea estaba fuera de la función y mal indentada
        self.assertIn("Saliendo del sistema...", salida_consola)

if __name__ == '__main__':
    unittest.main()