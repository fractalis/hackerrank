def skip_animals(animals, skip)
  ret = []
  animals.each_with_index { |item,index| ret << "#{index}:#{item}" if index >= skip }
  ret
end
