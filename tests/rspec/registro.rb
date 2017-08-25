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
                it 'Conexión con backend-animalitos' do
                  test =App.new('')
                  test.servicios('backend', '/test/conexion')
                  expect(test.response.code).to eq(200)
                end
            end
        end
    end
end

crear
