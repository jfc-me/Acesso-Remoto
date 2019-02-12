class Instrucoes():

    _result = ""
    _cmd = ""


    def _get_result(self):
        return self._result

    def _set_result(self,all_result):
        self._result = all_result

    def _get_cmd_lines(self):
        return self._cmd

    def _set_cmd_lines(self,cmd_line):
        self._cmd = cmd_line


    resultado = property(fset=_set_result, fget=_get_result)
    cmd = property(fset=_set_cmd_lines, fget=_get_cmd_lines)
