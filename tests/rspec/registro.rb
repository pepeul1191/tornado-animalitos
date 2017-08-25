# encoding: utf-8

require_relative 'app'
require 'json'

def crear
    file = File.new("data/registro_usuario.txt", "r")
    arreglo = []
    while (line = file.gets)
        data_json_string = line
        arreglo.push(data_json_string)
    end

    temp = nil
    k = 0
    RSpec.describe App do
        describe "1. Registrar Información Personal : " do
            arreglo.each do |url|
                it '1.1 Conexión con backend-animalitos' do
                  test =App.new('')
                  test.servicios('backend', '/test/conexion')
                  expect(test.response.code).to eq(200)
                end
                it '1.2 Registrar Información de Usuario' do
                    url = 'registro/guardar_usuario?data={"usuario":"pepex","contrasenia":"123","correo":"jaav@afpsdfa.com"}'
                    test = App.new(url)
                    test.post()
                    expect(test.response.body).not_to include('error')
                    expect(test.response.body).to include('Usuario registrado con éxito')
                end
            end
        end

    end
end

crear
