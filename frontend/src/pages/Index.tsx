
import React, { useState, useEffect } from 'react';
import { useMutation } from '@tanstack/react-query';
import { toast } from 'sonner';
import QuestionPanel from '../components/QuestionPanel';
import AnswerPanel from '../components/AnswerPanel';

type QueryPayload = { query: string };
type QueryResponse = { answer: string; detail?: string };

const Index = () => {
  const [dark, setDark] = useState(true);
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');

  useEffect(() => {
    document.documentElement.classList.toggle('dark', dark);
  }, [dark]);

  const mutation = useMutation({
    mutationFn: async (payload: QueryPayload): Promise<QueryResponse> => {
      const response = await fetch('http://localhost:8000/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Unknown error');
      return data;
    },
    onSuccess: (data) => setAnswer(data.answer),
    onError: (error: any) => {
      setAnswer(`Error: ${error.message || 'Unexpected error'}`);
      toast.error(`Error: ${error.message || 'Unexpected error'}`);
    }
  });

  const toggleDark = () => setDark(prev => !prev);

  const submitQuery = () => {
    if (!query.trim()) return;
    mutation.mutate({ query });
  };

  const copyAnswer = () => {
    if (!answer) return;
    navigator.clipboard.writeText(answer)
      .then(() => toast.success('Copied to clipboard!'))
      .catch(() => toast.error('Failed to copy to clipboard'));
  };

  const clearForm = () => {
    setQuery('');
    setAnswer('');
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-black text-white">
      <div className="container mx-auto px-4 py-8">
        <header className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent mb-2">
              Deep Research Agent
            </h1>
            <p className="text-gray-400">Powered by advanced AI for comprehensive research analysis</p>
          </div>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-1">
            <QuestionPanel
              query={query}
              setQuery={setQuery}
              submitQuery={submitQuery}
              copyAnswer={copyAnswer}
              hasAnswer={!!answer}
              clearForm={clearForm}
              isLoading={mutation.isPending}
            />
          </div>
          <div className="lg:col-span-2">
            <AnswerPanel loading={mutation.isPending} answer={answer} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;