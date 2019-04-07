class FahrenheitToCelsius
  def self.===(item)
    item[0] == "fahrenheit" && item[1] == "celsius"
  end
end

class FahrenheitToKelvin
  def self.===(item)
    item[0] == "fahrenheit" && item[1] == "kelvin"
  end
end

class FahrenheitToFahrenheit
  def self.===(item)
    item[0] == "fahrenheit" && item[1] == "fahrenheit"
  end
end

class CelsiusToKelvin
  def self.===(item)
    item[0] == "celsius" && item[1] == "kelvin"
  end
end

class CelsiusToCelsius
  def self.===(item)
    item[0] == "celsius" && item[1] == "celsius"
  end
end

class CelsiusToFahrenheit
  def self.===(item)
    item[0] == "celsius" && item[1] == "fahrenheit"
  end
end

class KelvinToCelsius
  def self.===(item)
    item[0] === "kelvin" && item[1] === "celsius"
  end
end

class KelvinToKelvin
  def self.===(item)
    item[0] == "kelvin" && item[1] == "kelvin"
  end
end

class KelvinToFahrenheit
  def self.===(item)
    item[0] == "kelvin" && item[1] == "fahrenheit"
  end
end

def convert_temp(input_temp, input_scale, output_scale="celsius")
  case [input_scale[:input_scale], input_scale[:output_scale]]
  when FahrenheitToCelsius
    (input_temp - 32) * 5.0/9.0
  when FahrenheitToKelvin
    (((input_temp - 32) * (5.0/9.0)) + 273.15)
  when FahrenheitToFahrenheit
    input_temp
  when CelsiusToKelvin
    input_temp + 273.15
  when CelsiusToCelsius
    input_temp
  when CelsiusToFahrenheit
    (input_temp * (9.0/5.0)) + 32
  when KelvinToKelvin
    input_temp
  when KelvinToCelsius
    input_temp - 273.15
  when KelvinToFahrenheit
    (input_temp - 273.15) * (9.0/5.0) + 32
  end
end
