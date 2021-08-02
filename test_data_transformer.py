from unittest.mock import Mock
from unittest.mock import patch
import readcsv
def test_data_transformer():
    mock_csv_reader = Mock()
    mock_json_saver = Mock()
    mock_csv_reader.return_value = [{},{},{}]
    
    readcsv.data_transformer('lol', 'woops', mock_csv_reader, mock_json_saver)
    assert mock_csv_reader.call_count == 1 
    mock_json_saver.assert_called_with([{'lol': 'woops'}, {'lol': 'woops'}, {'lol': 'woops'}])