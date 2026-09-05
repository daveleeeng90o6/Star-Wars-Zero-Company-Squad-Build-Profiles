-- Build: 57c0ec6ef4b782b3412d39a3eb7c024d
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
