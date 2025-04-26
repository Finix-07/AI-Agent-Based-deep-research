
import React from 'react';
import { Copy, Loader, Trash2 } from 'lucide-react';
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

interface QuestionPanelProps {
  query: string;
  setQuery: (query: string) => void;
  submitQuery: () => void;
  copyAnswer: () => void;
  hasAnswer: boolean;
  clearForm: () => void;
  isLoading: boolean;
}

const QuestionPanel: React.FC<QuestionPanelProps> = ({ 
  query, 
  setQuery, 
  submitQuery, 
  copyAnswer,
  hasAnswer,
  clearForm,
  isLoading
}) => {
  return (
    <div className="bg-white/5 backdrop-blur-lg rounded-2xl shadow-lg border border-white/10 p-6">
      <h2 className="text-lg font-semibold mb-4 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
        Your Question
      </h2>
      <Textarea
        className="min-h-[160px] mb-4 bg-white/5 border-white/10 backdrop-blur-sm text-white placeholder:text-gray-400"
        placeholder="Ask me anything about your research topic..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <div className="flex gap-3">
        <Button
          onClick={submitQuery}
          disabled={isLoading}
          className="flex-1 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white shadow-lg shadow-blue-700/20"
        >
          {isLoading ? (
            <>
              <Loader className="h-4 w-4 animate-spin mr-2" />
              Researching...
            </>
          ) : (
            'Research'
          )}
        </Button>
        <Button
          onClick={copyAnswer}
          disabled={!hasAnswer}
          variant="outline"
          className="border-white/10 bg-white/5 backdrop-blur-sm hover:bg-white/10"
        >
          <Copy className="h-4 w-4 mr-2" />
          Copy
        </Button>
        <Button
          onClick={clearForm}
          variant="outline"
          className="border-white/10 bg-white/5 backdrop-blur-sm hover:bg-white/10"
        >
          <Trash2 className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
};

export default QuestionPanel;