import React, { useEffect } from 'react';
import { Loader } from 'lucide-react';
import { marked } from 'marked';

interface AnswerPanelProps {
  loading: boolean;
  answer: string;
}

const AnswerPanel: React.FC<AnswerPanelProps> = ({ loading, answer }) => {
  // Configure marked to properly render markdown
  useEffect(() => {
    marked.setOptions({
      breaks: true, // Convert line breaks to <br>
      gfm: true, // Enable GitHub Flavored Markdown
      smartypants: true, // Use smart punctuation
      xhtml: true, // Render valid XHTML
    });
  }, []);

  return (
    <div className="bg-white/5 backdrop-blur-lg rounded-2xl shadow-lg border border-white/10 p-6 min-h-[500px] relative">
      <h2 className="text-lg font-semibold mb-4 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
        Research Findings
      </h2>
      <div className="relative">
        {loading && (
          <div className="absolute inset-0 flex items-center justify-center bg-black/20 backdrop-blur-sm rounded-lg z-10">
            <div className="flex flex-col items-center">
              <Loader className="animate-spin h-8 w-8 text-blue-400 mb-2" />
              <p className="text-sm text-blue-400">Researching...</p>
            </div>
          </div>
        )}
        <div className="prose prose-invert max-w-none prose-headings:text-blue-300 prose-a:text-purple-300 prose-code:bg-white/10 prose-code:p-1 prose-code:rounded prose-code:text-pink-300 prose-strong:text-yellow-300 prose-blockquote:border-l-4 prose-blockquote:border-blue-500 prose-blockquote:pl-4 prose-blockquote:italic prose-pre:bg-gray-800 prose-pre:rounded-lg prose-img:rounded-lg prose-li:marker:text-blue-400">
          {answer ? (
            <div dangerouslySetInnerHTML={{ __html: marked.parse(answer) }} />
          ) : (
            <div className="text-gray-400 italic">
              Your research findings will appear here...
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AnswerPanel;
