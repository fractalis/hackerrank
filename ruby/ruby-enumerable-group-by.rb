def group_by_marks(marks, pass_marks)
  marks.group_by do |x|
      x[1] <= pass_marks ? "Failed" : "Passed"
  end
end
