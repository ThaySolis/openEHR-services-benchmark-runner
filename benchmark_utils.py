import statistics
from scipy import stats
import datetime

def extract_versioned_object_id_from_version_id(version_id):
    """
    Extracts the versioned object identifier from the identifier of one of its versions.
    """

    version_id_parts = version_id.split("::")

    versioned_object_id = version_id_parts[0]

    return versioned_object_id

def time_formatted() -> str:
    return datetime.datetime.utcnow().replace(tzinfo=None).isoformat().replace("-", "").replace(":", "").replace(".", "")

def save_stats(sample : list, file_handle):
   # Este script calcula diversas estatísticas sobre um conjunto de números
   # fornecidos em sua entrada padrão ou em um arquivo indicado na linha de
   # comando (um número inteiro ou real por linha).
   #
   # Este script depende do módulo SciPy para Python 3.
   #
   # Carlos Maziero, Maio de 2020

   # erro fatal: numeros insuficientes na entrada
   if len(sample) < 2:
      raise ValueError("Erro: ao menos dois numeros devem ser fornecidos")

   # calcula média das amostras
   n       = len (sample)
   media   = statistics.mean (sample)	# media = sum (x) / n
   mediana = statistics.median (sample)	# mediana : x central na lista ordenada
   amin    = min (sample)
   amax    = max (sample)
   print ("numero de amostras\t\t= %d" % n, file = file_handle)
   print ("media das amostras\t\t= %f" % media, file = file_handle)
   print ("mediana das amostras\t\t= %f" % mediana, file = file_handle)
   print ("intervalo das amostras\t\t= [%f, %f]" % (amin, amax), file = file_handle)

   # calcula variancia populacao e amostra
   # vp = ( sum (x²) - (sum x)² / n ) / n		onde x é cada amostra
   # va = ( sum (x²) - (sum x)² / n ) / (n - 1)
   vp = statistics.pvariance (sample)
   va = statistics.variance  (sample)
   print ("variancia da populacao\t\t= %f" % vp, file = file_handle)
   print ("variancia das amostras\t\t= %f" % va, file = file_handle)

   # calcula desvios padrao população e amostra
   # dpp = math.sqrt (vp)
   # dpa = math.sqrt (va)
   dpp = statistics.pstdev (sample)
   dpa = statistics.stdev  (sample)
   print ("desvio padrao da populacao\t= %f" % dpp, file = file_handle)
   print ("desvio padrao das amostras\t= %f" % dpa, file = file_handle)

   # calcula coeficientes de variação
   cvp = 100.0 * dpp / media
   cva = 100.0 * dpa / media
   print ("coef variacao da populacao\t= %.2f%%" % cvp, file = file_handle)
   print ("coef variacao das amostras\t= %.2f%%" % cva, file = file_handle)

   # calcula erro padrão ou margem de erro das amostras
   # epa = dpa / math.sqrt (n)
   epa = stats.sem (sample)
   print ("erro padrao das amostras\t= %f" % epa, file = file_handle)

   # calcula intervalos de confiança das amostras (t-student, 2-tail)
   print ("Intervalos de confianca usando T-Student, 2-tails:", file = file_handle)
   for confid in (75, 90, 95, 99):
      alpha    = (1 + confid / 100.0) / 2
      tscore   = stats.t.ppf (alpha, n - 1)	# usa a tabela t-student
      linf     = media - tscore * epa
      lsup     = media + tscore * epa
      largura  = 100 * (lsup - linf) / media
      print ("interv confianca a %d%%\t\t= [%f, %f] (media ± %.2f%%)" % (confid, linf, lsup, largura/2), file = file_handle)
